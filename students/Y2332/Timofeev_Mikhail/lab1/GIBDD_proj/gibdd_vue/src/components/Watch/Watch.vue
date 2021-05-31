<template>
  <div v-if="currentItem" class="edit-form py-3">
    <p class="headline">Edit Watch</p>

    <v-form ref="form" lazy-validation>
      <v-select
            v-model="taken_car"
            :items="cars_number"
            :rules="[(v) => !!v || 'Car is required']"
            label="Car"
            required
        ></v-select>

        <v-select
            v-model="taken_inspector"
            :items="inspectors_number"
            :rules="[(v) => !!v || 'Inspector is required']"
            label="Inspector"
            required
        ></v-select>

        <v-date-picker
          v-model="currentItem.model"
          label="Date"
          min="1800-01-02"
          max="2021-12-31"
        ></v-date-picker>

        <v-text-field
          v-model="currentItem.sign_cost"
          :rules="[(v) => !!v || 'Sign cost is required']"
          label="Sign cost"
          required
        ></v-text-field>

        <v-text-field
          v-model="currentItem.watch_cost"
          :rules="[(v) => !!v || 'Watch cost is required']"
          label="Watch cost"
          required
        ></v-text-field>

        <v-checkbox
          v-model="currentItem.okay"
          label="Okay"
        ></v-checkbox>

        <v-text-field
          v-model="currentItem.reasons"
          v-if="!currentItem.okay"
          :rules="[(v) => !!v || 'Reasons is required']"
          label="Reasons"
          required
        ></v-text-field>

      <v-divider class="my-5"></v-divider>

      <v-btn color="success" small @click="updateItem">
        Update
      </v-btn>

      <v-btn color="error" small class="mr-2" @click="deleteItem">
        Delete
      </v-btn>

    </v-form>

    <p class="mt-3">{{ message }}</p>
  </div>

  <div v-else class="mx-auto">
    <p>Please click on a Watch...</p>
  </div>
</template>

<script>
import DataService from "@/services/DataService";

export default {
  name: "model",
  data() {
    return {
      currentItem: null,
      id: 0,
      cars: [],
      inspectors: [],
      cars_number: [],
      inspectors_number: [],
      taken_car: null,
      taken_inspector: null,
      message: "",
    };
  },
  methods: {
    getItem(id) {
      DataService.get(id)
        .then((response) => {
          let data = response.data.data;
          this.id = data.id;
          this.currentItem = {
            watch_date: data.attributes.watch_date,
            sign_cost: data.attributes.sign_cost,
            watch_cost: data.attributes.watch_cost,
            mileage: data.attributes.mileage,
            okay: data.attributes.okay,
            reasons: data.attributes.reasons,
            car_number: data.relationships.car_number.data.id,
            inspector: data.relationships.inspector.data.id,
          }
          this.taken_car = this.cars.find(x => x.id === this.currentItem.car_number).attributes.car_number;
          this.taken_inspector = this.inspectors.find(x => x.id === this.currentItem.inspector).attributes.sign_number;
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updateItem() {
      this.getInspectorIdByNumber();
      this.getCarIdByNumber();
      if (this.currentItem.okay)
        this.currentItem.reasons = "";
      console.log(this.currentItem);
      DataService.update(this.id, this.currentItem)
        .then((response) => {
          if (response.data.errors === undefined)
            this.message = "The watch was updated successfully!";
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        });
    },

    deleteItem() {
      DataService.delete(this.id)
        .then((response) => {
          console.log(response.data)
          this.$router.push({ name: "watch_list" });
        })
        .catch((e) => {
          console.log(e);
        });
    },

    async getAllInspectors(){
      DataService.setModelsName("inspectors");

      await DataService.getAll().then((response) => {
        this.inspectors = response.data.data;
        this.inspectors_number = this.inspectors.map(x => x.attributes.sign_number);
      });

      DataService.setModelsName("watch_info_list");
    },

    async getAllCars(){
      DataService.setModelsName("cars");

      await DataService.getAll().then((response) => {
        this.cars = response.data.data;
        this.cars_number = this.cars.map(x => x.attributes.car_number);
      });

      DataService.setModelsName("watch_info_list");
    },

    getCarIdByNumber(){
      this.currentItem.car_number = this.cars.find(x => this.taken_car === x.attributes.car_number).id;
    },

    getInspectorIdByNumber(){
      this.currentItem.inspector = this.inspectors.find(x => this.taken_inspector === x.attributes.sign_number).id;
    },
  },
  async mounted() {
    DataService.setModelsName("models")
    this.message = "";
    await this.getAllCars();
    await this.getAllInspectors();
    this.getItem(this.$route.params.id);
  },
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
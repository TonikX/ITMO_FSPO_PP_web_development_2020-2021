<template>
  <div v-if="currentItem" class="edit-form py-3">
    <p class="headline">Edit Away</p>

    <v-form ref="form" lazy-validation>
      <v-checkbox
        v-model="currentItem.driving_away"
        label="Awayed"
      ></v-checkbox>

      <v-date-picker
        v-model="currentItem.date_away"
        label="Date away"
        min="1800-01-01"
        max="2021-12-31"
      ></v-date-picker>

      <v-date-picker
        v-model="currentItem.date_return"
        v-if="!currentItem.driving_away"
        label="Date return"
        min="1800-01-02"
        max="2021-12-31"
      ></v-date-picker>

      <v-select
          v-model="taken_number"
          :items="cars_number"
          :rules="[(v) => !!v || 'Car is required']"
          label="Car"
          required
      ></v-select>

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

  <div v-else>
    <p>Please click on a Model...</p>
  </div>
</template>

<script>
import DataService from "../../services/DataService";

export default {
  name: "away",
  data() {
    return {
      currentItem: null,
      id: 0,
      cars: [],
      cars_number: [],
      taken_number: null,
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
            driving_away: data.attributes.driving_away,
            date_away: data.attributes.date_away,
            date_return: data.attributes.date_return,
            car_number: data.relationships.car_number.data.id,
          }
          this.taken_number = this.cars.find(x => x.id === this.currentItem.car_number).attributes.car_number;
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updateItem() {
      this.setCarIdByNumber();
      if (this.currentItem.driving_away)
        this.currentItem.date_return = null;
      DataService.update(this.id, this.currentItem)
        .then((response) => {
          if (response.data.errors === undefined)
            this.message = "The away was updated successfully!";
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        });
    },

    deleteItem() {
      DataService.delete(this.id)
        .then((response) => {
          console.log(response.data)
          this.$router.push({ name: "drive_away_info_list" });
        })
        .catch((e) => {
          console.log(e);
        });
    },

    async getAllCars(){
      DataService.setModelsName("cars");

      await DataService.getAll().then((response) => {
        this.cars = response.data.data
        this.cars_number = this.cars.map(x => x.attributes.car_number);
      });

      DataService.setModelsName("drive_away_info_list");
    },

    setCarIdByNumber(){
      this.currentItem.car_number = this.cars.find(x => this.taken_number === x.attributes.car_number).id;
    },
  },
  async mounted() {
    DataService.setModelsName("drive_away_info_list")
    this.message = "";
    await this.getAllCars();
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
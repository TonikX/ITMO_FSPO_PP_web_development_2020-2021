<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Add Watch</p>

    <div v-if="!submitted">
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
          v-model="currentItem.watch_date"
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
          v-model="currentItem.mileage"
          :rules="[(v) => !!v || 'Mileage is required']"
          label="Mileage"
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

        <v-btn color="primary" class="mt-3" @click="saveItem">Submit</v-btn>
      </v-form>
    </div>

    <div v-else-if="submitted">
      <v-card class="mx-auto">
        <v-card-title>
          Submitted successfully!
        </v-card-title>

        <v-card-subtitle>
          Click the button to add new Watch.
        </v-card-subtitle>

        <v-card-actions>
          <v-btn color="success" @click="newItem">Add</v-btn>
        </v-card-actions>
      </v-card>
    </div>

    <p class="mt-3">{{ this.message }}</p>
  </div>
</template>

<script>
import DataService from "../../services/DataService";

export default {
  name: "add-watch",
  data() {
    return {
      currentItem: {
        watch_date: null,
        sign_cost: 0,
        watch_cost: 0,
        mileage: 0,
        okay: false,
        reasons: "",
        car_number: 0,
        inspector: 0,
      },
      cars_number: [],
      inspectors_number: [],
      cars: [],
      inspectors: [],
      taken_car: null,
      taken_inspector: null,
      submitted: false,
      message: ''
    };
  },
  methods: {
    saveItem() {
      this.getInspectorIdByNumber();
      this.getCarIdByNumber();
      if (this.currentItem.okay)
        this.currentItem.reasons = "";
      console.log(this.currentItem);
      DataService.create(this.currentItem)
        .then((response) => {
          this.message = ''
          this.submitted = true;
          console.log(response.data);
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        });
    },

    newItem() {
      this.submitted = false;
      this.message = '';
      this.currentItem = {};
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
      DataService.setModelsName("watch_info_list");
      await this.getAllCars();
      await this.getAllInspectors();
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
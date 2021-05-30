<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Add away</p>

    <div v-if="!submitted">
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

        <v-btn color="primary" class="mt-3" @click="saveItem">Submit</v-btn>
      </v-form>
    </div>

    <div v-else-if="submitted">
      <v-card class="mx-auto">
        <v-card-title>
          Submitted successfully!
        </v-card-title>

        <v-card-subtitle>
          Click the button to add new Away.
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
  name: "add-away",
  data() {
    return {
      currentItem: {
        driving_away: false,
        date_away: null,
        date_return: null,
        car_number: 0,
      },
      cars: [],
      cars_number: [],
      taken_number: null,
      submitted: false,
      message: ''
    };
  },
  methods: {
    saveItem() {
      this.setCarIdByNumber();
      if (this.currentItem.driving_away)
        this.currentItem.date_return = null;
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

    getAllCars(){
      DataService.setModelsName("cars");

      DataService.getAll().then((response) => {
        this.cars = response.data.data
        this.cars_number = this.cars.map(x => x.attributes.car_number);
      });

      DataService.setModelsName("drive_away_info_list");
    },

    setCarIdByNumber(){
      this.currentItem.car_number = this.cars.find(x => this.taken_number === x.attributes.car_number).id;
    },
  },
  mounted() {
      DataService.setModelsName("drive_away_info_list");
      this.getAllCars();
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
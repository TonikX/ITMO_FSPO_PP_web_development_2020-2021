<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Add Engine</p>

    <div v-if="!submitted">
      <v-form ref="form" lazy-validation>
        <v-text-field
          v-model="item.engine_type"
          :rules="[(v) => !!v || 'Type is required']"
          label="Type"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.power"
          :rules="[(v) => !!v || 'Power is required']"
          label="Power"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.volume"
          :rules="[(v) => !!v || 'Volume is required']"
          label="Volume"
          required
        ></v-text-field>
      </v-form>

      <v-btn color="primary" class="mt-3" @click="saveItem">Submit</v-btn>
    </div>

    <div v-else-if="submitted">
      <v-card class="mx-auto">
        <v-card-title>
          Submitted successfully!
        </v-card-title>

        <v-card-subtitle>
          Click the button to add new Engine.
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
  name: "add-engine",
  data() {
    return {
      item: {
        engine_type: "",
        power: 0,
        value: 0
      },
      submitted: false,
      message: ''
    };
  },
  methods: {
    saveItem() {
      DataService.create(this.item)
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
      this.item = {};
    },


  },
  mounted() {
      DataService.setModelsName("engines")
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
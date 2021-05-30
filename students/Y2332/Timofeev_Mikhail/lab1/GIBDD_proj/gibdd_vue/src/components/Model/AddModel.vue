<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Add Model</p>

    <div v-if="!submitted">
      <v-form ref="form" lazy-validation>
        <v-text-field
          v-model="item.model"
          :rules="[(v) => !!v || 'Model is required']"
          label="Model"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.brand"
          :rules="[(v) => !!v || 'Brand is required']"
          label="Brand"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.producer"
          :rules="[(v) => !!v || 'Producer is required']"
          label="Producer"
          required
        ></v-text-field>

        <v-select
            v-model="taken_body_model"
            :items="bodies_model"
            :rules="[(v) => !!v || 'Body is required']"
            label="Body"
            required
        ></v-select>

        <v-select
            v-model="taken_engine_type"
            :items="engines_type"
            :rules="[(v) => !!v || 'Engine is required']"
            label="Engine"
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
          Click the button to add new Model.
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
  name: "add-body",
  data() {
    return {
      item: {
        model: "",
        brand: "",
        producer: "",
        body_id: 0,
        engine_id: 0
      },
      bodies_model: [],
      engines_type: [],
      bodies: [],
      engines: [],
      taken_engine_type: null,
      taken_body_model: null,
      submitted: false,
      message: ''
    };
  },
  methods: {
    saveItem() {
      this.getBodyIdByType();
      this.getEngineIdByType();
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

    getAllBodies(){
      DataService.setModelsName("bodies");

      DataService.getAll().then((response) => {
        this.bodies = response.data.data
        this.bodies_model = this.bodies.map(x => x.attributes.body_model);
      });

      DataService.setModelsName("models");
    },

    getAllEngines(){
      DataService.setModelsName("engines");

      DataService.getAll().then((response) => {
        this.engines = response.data.data
        this.engines_type = this.engines.map(x => x.attributes.engine_type);
      });

      DataService.setModelsName("models");
    },

    getEngineIdByType(){
      this.item.engine_id = this.engines.find(x => this.taken_engine_type === x.attributes.engine_type).id;
    },

    getBodyIdByType(){
      this.item.body_id = this.bodies.find(x => this.taken_body_model === x.attributes.body_model).id;
    },
  },
  mounted() {
      DataService.setModelsName("models");
      this.getAllEngines();
      this.getAllBodies();
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
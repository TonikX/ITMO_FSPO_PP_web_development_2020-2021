<template>
  <div v-if="currentItem" class="edit-form py-3">
    <p class="headline">Edit Model</p>

    <v-form ref="form" lazy-validation>
      <v-text-field
        v-model="currentItem.model"
        :rules="[(v) => !!v || 'Model is required']"
        label="Model"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.brand"
        :rules="[(v) => !!v || 'Brand is required']"
        label="Brand"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.producer"
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
  name: "model",
  data() {
    return {
      currentItem: null,
      id: 0,
      bodies_model: [],
      engines_type: [],
      taken_engine_type: null,
      taken_body_model: null,
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
            model: data.attributes.model,
            brand: data.attributes.brand,
            producer: data.attributes.producer,
            body_id: data.relationships.body_id.data.id,
            engine_id: data.relationships.engine_id.data.id,
          }
          this.taken_engine_type = this.engines.find(x => x.id === this.currentItem.engine_id).attributes.engine_type;
          this.taken_body_model = this.bodies.find(x => x.id === this.currentItem.body_id).attributes.body_model;
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updateItem() {
      this.setBodyIdByType();
      this.setEngineIdByType();
      console.log(this.currentItem);
      DataService.update(this.id, this.currentItem)
        .then((response) => {
          if (response.data.errors === undefined)
            this.message = "The model was updated successfully!";
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        });
    },

    deleteItem() {
      DataService.delete(this.id)
        .then((response) => {
          console.log(response.data)
          this.$router.push({ name: "models" });
        })
        .catch((e) => {
          console.log(e);
        });
    },

    async getAllBodies(){
      DataService.setModelsName("bodies");

      await DataService.getAll().then((response) => {
        this.bodies = response.data.data
        this.bodies_model = this.bodies.map(x => x.attributes.body_model);
      });

      DataService.setModelsName("models");
    },

    async getAllEngines(){
      DataService.setModelsName("engines");

      await DataService.getAll().then((response) => {
        this.engines = response.data.data
        this.engines_type = this.engines.map(x => x.attributes.engine_type);
      });

      DataService.setModelsName("models");
    },

    setEngineIdByType(){
      this.currentItem.engine_id = this.engines.find(x => this.taken_engine_type === x.attributes.engine_type).id;
    },

    setBodyIdByType(){
      this.currentItem.body_id = this.bodies.find(x => this.taken_body_model === x.attributes.body_model).id;
    },
  },
  async mounted() {
    DataService.setModelsName("models")
    this.message = "";
    await this.getAllBodies();
    await this.getAllEngines();
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
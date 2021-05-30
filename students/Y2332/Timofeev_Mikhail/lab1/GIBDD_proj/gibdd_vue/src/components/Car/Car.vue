<template>
  <div v-if="currentItem" class="edit-form py-3">
    <p class="headline">Edit Car</p>

    <v-form ref="form" lazy-validation>
      <v-text-field
        v-model="currentItem.car_number"
        :rules="[(v) => !!v || 'Number is required']"
        label="Number"
        required
      ></v-text-field>

      <v-select
          v-model="taken_model"
          :items="models_model"
          :rules="[(v) => !!v || 'Model is required']"
          label="Model"
          required
      ></v-select>

      <v-checkbox
          v-model="currentItem.helm"
          label="Helm"
      ></v-checkbox>

      <v-checkbox
          v-model="currentItem.drive"
          label="Drive"
      ></v-checkbox>

      <v-text-field
        v-model="currentItem.color"
        :rules="[(v) => !!v || 'Color is required']"
        label="Color"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.district"
        :rules="[(v) => !!v || 'District is required']"
        label="District"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.year"
        :rules="[(v) => !!v || 'Year is required']"
        label="Year"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.year_tax"
        :rules="[(v) => !!v || 'Year tax is required']"
        label="Year tax"
        required
      ></v-text-field>

      <v-select
          v-model="taken_id"
          :items="physicals_id"
          label="Physical owner"
      ></v-select>

      <v-select
          v-model="taken_inn"
          :items="legals_inn"
          label="Legal owner"
      ></v-select>

      <v-text-field
        v-model="currentItem.comment"
        label="Comment"
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

  <div v-else>
    <p>Please click on a Car...</p>
  </div>
</template>

<script>
import DataService from "../../services/DataService";

export default {
  name: "car",
  data() {
    return {
      currentItem: null,
      id: 0,
      models_model: [],
      legals_inn: [],
      physicals_id: [],
      taken_model: null,
      taken_id: null,
      taken_inn: null,
      message: "",
    };
  },
  methods: {
    getItem(id) {
      DataService.get(id)
        .then((response) => {
          let data = response.data.data;
          let ownerINN = data.relationships.owner_inn.data;
          let ownerID = data.relationships.owner_id.data;
          this.id = data.id;
          this.currentItem = {
            car_number: data.attributes.car_number,
            helm: data.attributes.helm,
            drive: data.attributes.drive,
            year: data.attributes.year,
            owner_type: data.attributes.owner_type,
            district: data.attributes.district,
            year_tax: data.attributes.year_tax,
            comment: data.attributes.comment,
            color: data.attributes.color,
            model: data.relationships.model.data.id,
            owner_inn: ownerINN == null ? null : ownerINN.id,
            owner_id: ownerID == null ? null : ownerID.id,
          }
          this.taken_model = this.models.find(x => x.id === this.currentItem.model).attributes.model;

          if (this.currentItem.owner_inn != null)
            this.taken_inn = this.legal_owners.find(x => x.id === this.currentItem.owner_inn).attributes.owner_inn;
          else
            this.taken_id = this.physical_owners.find(x => x.id === this.currentItem.owner_id).attributes.owner_id;
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updateItem() {
      this.setModelByModel();
      if (this.taken_inn != null && this.taken_inn !== "") {
        this.setLOwnerByLOwerINN();
      }
      else if (this.taken_id != null && this.taken_id !== "") {
        this.setPOwnerByPOwnerID();
      }
      else {
        this.message = "Owner is required";
        return;
      }
      DataService.update(this.id, this.currentItem)
        .then((response) => {
          if (response.data.errors === undefined)
            this.message = "The car was updated successfully!";
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        });
    },

    deleteItem() {
      DataService.delete(this.id)
        .then((response) => {
          console.log(response.data)
          this.$router.push({ name: "cars" });
        })
        .catch((e) => {
          console.log(e);
        });
    },

    async getAllLOwners(){
      DataService.setModelsName("legal_owners");

      this.legals_inn.push("");

      await DataService.getAll().then((response) => {
        this.legal_owners = response.data.data;
        this.legals_inn = this.legals_inn.concat(this.legal_owners.map(x => x.attributes.owner_inn));
      });

      DataService.setModelsName("cars");
    },

    async getAllPOwners(){
      DataService.setModelsName("physical_owners");

      this.physicals_id.push("");

      await DataService.getAll().then((response) => {
        this.physical_owners = response.data.data;
        this.physicals_id = this.physicals_id.concat(this.physical_owners.map(x => x.attributes.owner_id));
      });

      DataService.setModelsName("cars");
    },

    async getAllModels(){
      DataService.setModelsName("models");

      await DataService.getAll().then((response) => {
        this.models = response.data.data;
        this.models_model = this.models.map(x => x.attributes.model);
      });

      DataService.setModelsName("cars");
    },

    setModelByModel(){
      this.currentItem.model = this.models.find(x => this.taken_model === x.attributes.model).id;
    },

    setPOwnerByPOwnerID(){
      this.currentItem.owner_id = this.physical_owners.find(x => this.taken_id === x.attributes.owner_id).id;
      this.currentItem.owner_inn = null
    },

    setLOwnerByLOwerINN(){
      this.currentItem.owner_inn = this.legal_owners.find(x => this.taken_inn === x.attributes.owner_inn).id;
      this.currentItem.owner_id = null;
    },
  },
  async mounted() {
    DataService.setModelsName("cars")
    this.message = "";
    await this.getAllLOwners();
    await this.getAllPOwners();
    await this.getAllModels();
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
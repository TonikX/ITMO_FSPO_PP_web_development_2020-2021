<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Add Car</p>

    <div v-if="!submitted">
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

        <v-btn color="primary" class="mt-3" @click="saveItem">Submit</v-btn>
      </v-form>
    </div>

    <div v-else-if="submitted">
      <v-card class="mx-auto">
        <v-card-title>
          Submitted successfully!
        </v-card-title>

        <v-card-subtitle>
          Click the button to add new Car.
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
      currentItem: {
        car_number: "",
        helm: false,
        drive: false,
        year: 1800,
        owner_type: false,
        district: "",
        year_tax: 0,
        comment: "",
        color: "",
        model: 0,
        owner_inn: 0,
        owner_id: 0,
      },
      models_model: [],
      legals_inn: [],
      physicals_id: [],
      taken_model: null,
      taken_id: null,
      taken_inn: null,
      models: [],
      legal_owners: [],
      physical_owners: [],
      submitted: false,
      message: ''
    };
  },
  methods: {
    saveItem() {
      this.setModelByModel();
      if (this.taken_inn != null && this.taken_inn !== "") {
        this.setLOwnerByLOwerINN();
      }
      else if (this.taken_id != null && this.taken_id !== "") {
        this.setPOwnerByPOwnerID();
      }

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

    getAllLOwners(){
      DataService.setModelsName("legal_owners");

      this.legals_inn.push("");

      DataService.getAll().then((response) => {
        this.legal_owners = response.data.data;
        this.legals_inn = this.legals_inn.concat(this.legal_owners.map(x => x.attributes.owner_inn));
      });

      DataService.setModelsName("cars");
    },

    getAllPOwners(){
      DataService.setModelsName("physical_owners");

      this.physicals_id.push("");

      DataService.getAll().then((response) => {
        this.physical_owners = response.data.data;
        this.physicals_id = this.physicals_id.concat(this.physical_owners.map(x => x.attributes.owner_id));
      });

      DataService.setModelsName("cars");
    },

    getAllModels(){
      DataService.setModelsName("models");

      DataService.getAll().then((response) => {
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
  mounted() {
      DataService.setModelsName("models");
      this.getAllLOwners();
      this.getAllPOwners();
      this.getAllModels();
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
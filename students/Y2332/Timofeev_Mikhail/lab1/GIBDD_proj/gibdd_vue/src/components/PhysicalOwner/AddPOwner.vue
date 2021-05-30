<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Add Legal Owner</p>

    <div v-if="!submitted">
      <v-form ref="form" lazy-validation>
        <v-text-field
          v-model="item.owner_id"
          :rules="[(v) => !!v || 'ID is required']"
          label="ID"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.owner_fullname"
          :rules="[(v) => !!v || 'Name is required']"
          label="Name"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.phone"
          :rules="[(v) => !!v || 'Phone is required']"
          label="Phone"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.address"
          :rules="[(v) => !!v || 'Address is required']"
          label="Address"
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
          Click the button to add new Physical Owner.
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
  name: "add-pOwner",
  data() {
    return {
      item: {
        owner_id: 100000,
        owner_fullname: "",
        phone: "",
        address: "",
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
      DataService.setModelsName("physical_owners")
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
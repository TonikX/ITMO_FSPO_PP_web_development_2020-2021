<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Add Inspector</p>

    <div v-if="!submitted">
      <v-form ref="form" lazy-validation>
        <v-text-field
          v-model="item.sign_number"
          :rules="[(v) => !!v || 'Sign number is required']"
          label="Sign number"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.fullname"
          :rules="[(v) => !!v || 'Name is required']"
          label="Name"
          required
        ></v-text-field>

        <v-text-field
          v-model="item.post"
          :rules="[(v) => !!v || 'Post is required']"
          label="Post"
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
          Click the button to add new Inspector.
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
  name: "add-inspector",
  data() {
    return {
      item: {
        sign_number: "",
        fullname: "",
        post: ""
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
      DataService.setModelsName("inspectors")
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
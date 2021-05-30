<template>
  <div v-if="currentItem" class="edit-form py-3">
    <p class="headline">Edit Inspector</p>

    <v-form ref="form" lazy-validation>
      <v-text-field
        v-model="currentItem.attributes.sign_number"
        :rules="[(v) => !!v || 'Sign number is required']"
        label="Sign number"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.attributes.fullname"
        :rules="[(v) => !!v || 'Name is required']"
        label="Name"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.attributes.post"
        :rules="[(v) => !!v || 'Post is required']"
        label="Post"
        required
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
    <p>Please click on a Inspector...</p>
  </div>
</template>

<script>
import DataService from "../../services/DataService";

export default {
  name: "engine",
  data() {
    return {
      currentItem: null,
      message: "",
    };
  },
  methods: {
    getItem(id) {
      DataService.get(id)
        .then((response) => {
          this.currentItem = response.data.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updateItem() {
      DataService.update(this.currentItem.id, this.currentItem.attributes)
        .then((response) => {
          if (response.data.errors === undefined)
            this.message = "The inspector was updated successfully!";
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        });
    },

    deleteItem() {
      DataService.delete(this.currentItem.id)
        .then((response) => {
          console.log(response.data)
          this.$router.push({ name: "inspectors" });
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  mounted() {
    DataService.setModelsName("inspectors");
    this.message = "";
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
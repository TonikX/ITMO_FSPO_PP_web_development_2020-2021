<template>
  <div v-if="currentItem" class="edit-form py-3">
    <p class="headline">Edit Body</p>

    <v-form ref="form" lazy-validation>
      <v-text-field
        v-model="currentItem.attributes.body_model"
        :rules="[(v) => !!v || 'Model is required']"
        label="Model"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.attributes.body_type"
        :rules="[(v) => !!v || 'Type is required']"
        label="Type"
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
    <p>Please click on a Body...</p>
  </div>
</template>

<script>
import DataService from "../../services/DataService";

export default {
  name: "body",
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
            this.message = "The body was updated successfully!";
        })
        .catch((e) => {
          console.log(e);
        });
    },

    deleteItem() {
      DataService.delete(this.currentItem.id)
        .then((response) => {
          console.log(response.data)
          this.$router.push({ name: "bodies" });
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  mounted() {
    DataService.setModelsName("bodies")
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
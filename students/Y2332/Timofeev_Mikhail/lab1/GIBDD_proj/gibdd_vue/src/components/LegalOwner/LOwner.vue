<template>
  <div v-if="currentItem" class="edit-form py-3">
    <p class="headline">Edit Legal Owner</p>

    <v-form ref="form" lazy-validation>
      <v-text-field
        v-model="currentItem.attributes.owner_inn"
        :rules="[(v) => !!v || 'INN is required']"
        label="INN"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.attributes.owner_name"
        :rules="[(v) => !!v || 'Name is required']"
        label="Name"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.attributes.chief"
        :rules="[(v) => !!v || 'Chief is required']"
        label="Chief"
        required
      ></v-text-field>

      <v-text-field
        v-model="currentItem.attributes.phone"
        :rules="[(v) => !!v || 'Phone is required']"
        label="Phone"
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
    <p>Please click on a Legal Owner...</p>
  </div>
</template>

<script>
import DataService from "../../services/DataService";

export default {
  name: "lOwner",
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
            this.message = "The legal owner was updated successfully!";
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        });
    },

    deleteItem() {
      DataService.delete(this.currentItem.id)
        .then((response) => {
          console.log(response.data)
          this.$router.push({ name: "lOwners" });
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  mounted() {
    DataService.setModelsName("legal_owners")
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
<template>
  <v-row align="center" class="list px-3 mx-auto">
    <v-col cols="12" md="8">
      <v-text-field v-model="search" label="Search"></v-text-field>
    </v-col>

    <v-col cols="12" md="4">
      <v-btn small @click="page = 1; searchBy();">
        Search
      </v-btn>
    </v-col>

     <v-col cols="12" sm="12">
      <v-row>
        <v-col cols="4" sm="3">
          <v-select
            v-model="pageSize"
            :items="pageSizes"
            label="Items per Page"
            @change="handlePageSizeChange"
          ></v-select>
        </v-col>

        <v-col cols="12" sm="9">
          <v-pagination
            v-model="page"
            :length="totalPages"
            total-visible="7"
            next-icon="mdi-menu-right"
            prev-icon="mdi-menu-left"
            @input="handlePageChange"
          ></v-pagination>
        </v-col>
      </v-row>
    </v-col>

    <v-col cols="12" sm="12">
      <v-card class="mx-auto" tile>
        <v-card-title>Models</v-card-title>

        <v-data-table
          :headers="headers"
          :items="items"
          disable-pagination
          :hide-default-footer="true"
        >
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon small class="mr-2" @click="editItem(item.id)">mdi-pencil</v-icon>
            <v-icon small @click="deleteItem(item.id)">mdi-delete</v-icon>
          </template>
          <template v-slot:[`item.body_model`]="{ item }">
            <p @click="editBody(item.body_id)">{{item.body_model}}</p>
          </template>
          <template v-slot:[`item.engine_type`]="{ item }">
            <p @click="editEngine(item.engine_id)">{{item.engine_type}}</p>
          </template>
        </v-data-table>

        <v-card-actions>
          <v-btn small color="success" @click="addItem">
            Add
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import DataService from "../../services/DataService";
export default {
  name: "models-list",
  data() {
    return {
      items: [],
      search: "",
      headers: [
        { text: "Model", align: "start", value: "model", sortable: false },
        { text: "Brand", value: "brand", sortable: false },
        { text: "Producer", value: "producer", sortable: false },
        { text: "Body", value: "body_model", sortable: false },
        { text: "Engine", value: "engine_type", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
      bodies: [],
      engines: [],

      page: 1,
      totalPages: 0,
      pageSize: 3,
      totalVisible: 0,

      pageSizes: [3, 6, 9],
    };
  },
  methods: {
    retrieveItems() {
      DataService.getAll()
        .then((response) => {
          this.items = response.data.data.map(this.getDisplayModel);
          this.totalPages = Math.ceil(this.items.length / this.pageSize);
          this.items = this.items.slice((this.page-1)*this.pageSize, this.page*this.pageSize)
        })
        .catch((e) => {
          console.log(e);
        });
    },

    handlePageChange(value) {
      this.page = value;
      if (this.search === "")
        this.retrieveItems();
      else
        this.searchBy(this.search);
    },

    handlePageSizeChange(size) {
      this.pageSize = size;
      this.page = 1;
      if (this.search === "")
        this.retrieveItems();
      else
        this.searchBy(this.search);
    },

    refreshList() {
      this.retrieveItems();
    },

    addItem() {
      this.$router.push({ name: "add-model" });
    },

    searchBy() {
      DataService.find(this.search)
        .then((response) => {
          this.items = response.data.data.map(this.getDisplayModel);
          this.totalPages = Math.ceil(this.items.length / this.pageSize);
          this.items = this.items.slice((this.page-1)*this.pageSize, this.page*this.pageSize)
        })
        .catch((e) => {
          console.log(e);
        });
    },

    editItem(id) {
      this.$router.push({ name: "model", params: { id: id } });
    },

    editEngine(id){
      this.$router.push({ name: "engine", params: { id: id } });
    },

    editBody(id){
      this.$router.push({ name: "body", params: { id: id } });
    },

    deleteItem(id) {
      DataService.delete(id)
        .then(() => {
          this.refreshList();
        })
        .catch((e) => {
          console.log(e);
        });
    },

    getDisplayModel(model) {
      let attributes = model.attributes;
      let relation = model.relationships;
      let bodyId = relation.body_id.data.id;
      let engineId = relation.engine_id.data.id;
      let bodyModel = this.bodies.find(x => x.id === `${bodyId}`).attributes.body_model;
      let engineType = this.engines.find(x => x.id === `${engineId}`).attributes.engine_type;
      return {
        id: model.id,
        model: attributes.model,
        brand: attributes.brand,
        producer: attributes.producer,
        body_id: bodyId,
        engine_id: engineId,
        body_model: bodyModel,
        engine_type: engineType,
      };
    },
    async getAllBodies(){
      DataService.setModelsName("bodies");

      await DataService.getAll().then((response) => {
        this.bodies = response.data.data;
      });

      DataService.setModelsName("models");
    },

    async getAllEngines(){
      DataService.setModelsName("engines");

      await DataService.getAll().then((response) => {
        this.engines = response.data.data;
      });

      DataService.setModelsName("models");
    },
  },
  async mounted() {
    DataService.setModelsName("models");
    await this.getAllEngines();
    await this.getAllBodies();
    this.retrieveItems();
  },
};
</script>

<style>
.list {
  max-width: 750px;
}
</style>
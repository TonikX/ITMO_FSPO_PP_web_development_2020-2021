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
        <v-card-title>Cars</v-card-title>

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
          <template v-slot:[`item.lOwnerINN`]="{ item }">
            <p @click="editLOwner(item.owner_inn)">{{item.lOwnerINN}}</p>
          </template>
          <template v-slot:[`item.pOwnerId`]="{ item }">
            <p @click="editPOwner(item.owner_id)">{{item.pOwnerId}}</p>
          </template>
          <template v-slot:[`item.carModel`]="{ item }">
            <p @click="editModel(item.model)">{{item.carModel}}</p>
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
  name: "cars-list",
  data() {
    return {
      items: [],
      search: "",
      headers: [
        { text: "Number", align: "start", value: "car_number", sortable: false },
        { text: "Model", value: "carModel", sortable: false },
        { text: "Helm", value: "helm", sortable: false },
        { text: "Drive", value: "drive", sortable: false },
        { text: "Color", value: "color", sortable: false },
        { text: "District", value: "district", sortable: false },
        { text: "Year", value: "year", sortable: false },
        { text: "Year tax", value: "year_tax", sortable: false },
        { text: "LOwner", value: "lOwnerINN", sortable: false },
        { text: "POwner", value: "pOwnerId", sortable: false },
        { text: "Comment", value: "comment", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
      models: [],
      legal_owners: [],
      physical_owners: [],

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
      this.$router.push({ name: "add-car" });
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
      this.$router.push({ name: "car", params: { id: id } });
    },

    editLOwner(id){
      this.$router.push({ name: "lOwner", params: { id: id } });
    },

    editPOwner(id){
      this.$router.push({ name: "pOwner", params: { id: id } });
    },

    editModel(id){
      this.$router.push({ name: "model", params: { id: id } });
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
      let modelId = relation.model.data.id;
      let lOwnerId = relation.owner_inn.data;
      let lOwnerINN = null;
      if (lOwnerId != null) {
        lOwnerId = lOwnerId.id;
        lOwnerINN = this.legal_owners.find(x => x.id === `${lOwnerId}`).attributes.owner_inn;
      }
      let pOwnerId = relation.owner_id.data;
      let pOwnerINN = null;
      if (pOwnerId != null) {
        pOwnerId = pOwnerId.id;
        pOwnerINN = this.physical_owners.find(x => x.id === `${pOwnerId}`).attributes.owner_id;
      }
      let carModel = this.models.find(x => x.id === `${modelId}`).attributes.model;
      return {
        id: model.id,
        car_number: attributes.car_number,
        helm: attributes.helm,
        drive: attributes.drive,
        year: attributes.year,
        owner_type: attributes.owner_type,
        district: attributes.district,
        year_tax: attributes.year_tax,
        comment: attributes.comment,
        color: attributes.color,
        model: modelId,
        owner_inn: lOwnerId,
        owner_id: pOwnerId,
        carModel: carModel,
        lOwnerINN: lOwnerINN,
        pOwnerId: pOwnerINN,
      };
    },
    async getAllLOwners(){
      DataService.setModelsName("legal_owners");

      await DataService.getAll().then((response) => {
        this.legal_owners = response.data.data;
      });

      DataService.setModelsName("cars");
    },

    async getAllPOwners(){
      DataService.setModelsName("physical_owners");

      await DataService.getAll().then((response) => {
        this.physical_owners = response.data.data;
      });

      DataService.setModelsName("cars");
    },

    async getAllModels(){
      DataService.setModelsName("models");

      await DataService.getAll().then((response) => {
        this.models = response.data.data;
      });

      DataService.setModelsName("cars");
    },
  },
  async mounted() {
    DataService.setModelsName("cars");
    await this.getAllPOwners();
    await this.getAllLOwners();
    await this.getAllModels();
    this.retrieveItems();
  },
};
</script>

<style>
.list {
  max-width: 750px;
}
</style>
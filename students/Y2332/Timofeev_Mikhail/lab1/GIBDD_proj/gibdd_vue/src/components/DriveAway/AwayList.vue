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
        <v-card-title>Drive aways</v-card-title>

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
          <template v-slot:[`item.car_number_number`]="{ item }">
            <p @click="editCar(item.car_number)">{{item.car_number_number}}</p>
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
  name: "away-list",
  data() {
    return {
      items: [],
      search: "",
      headers: [
        { text: "Awayed", align: "start", value: "driving_away", sortable: false },
        { text: "Date away", value: "date_away", sortable: false },
        { text: "Date return", value: "date_return", sortable: false },
        { text: "Car", value: "car_number_number", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
      cars: [],

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
      this.$router.push({ name: "add-away" });
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

    editCar(id) {
      this.$router.push({ name: "car", params: { id: id } });
    },

    editItem(id) {
      this.$router.push({ name: "away", params: { id: id } });
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
      let carNumber = relation.car_number.data.id;
      let carNumberNumber = this.cars.find(x => x.id === `${carNumber}`).attributes.car_number;
      return {
        id: model.id,
        driving_away: attributes.driving_away,
        date_away: attributes.date_away,
        date_return: attributes.date_return,
        car_number: carNumber,
        car_number_number: carNumberNumber,
      };
    },

    async getAllCars(){
      DataService.setModelsName("cars");

      await DataService.getAll().then((response) => {
        this.cars = response.data.data
      });

      DataService.setModelsName("drive_away_info_list");
    },
  },
  async mounted() {
    DataService.setModelsName("models");
    await this.getAllCars();
    this.retrieveItems();
  },
};
</script>

<style>
.list {
  max-width: 750px;
}
</style>
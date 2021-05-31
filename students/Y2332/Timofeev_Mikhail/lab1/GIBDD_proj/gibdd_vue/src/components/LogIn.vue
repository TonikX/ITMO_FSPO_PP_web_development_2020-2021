<template>
  <div class="edit-form py-3">
    <p class="headline">Log in</p>

    <v-form ref="form" lazy-validation>
      <v-text-field
        v-model="user.username"
        :rules="[(v) => !!v || 'Username is required']"
        label="Username"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.password"
        :append-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[password_rules.required, password_rules.min]"
        :type="show_password ? 'text' : 'password'"
        label="Password"
        hint="At least 8 characters"
        counter
        @click:append="show_password = !show_password"
      ></v-text-field>

      <v-divider class="my-5"></v-divider>

      <v-btn color="success" small @click="logIn">
        Log in
      </v-btn>

    </v-form>

    <p class="mt-3">{{ message }}</p>
  </div>
</template>

<script>
import AuthorizationService from "@/services/AuthorizationService";
import DataService from "@/services/DataService";

export default {
  name: "logIn",
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
      password_rules: {
        required: value => !!value || 'Password is required',
        min: v => v.length >= 8 || 'Min 8 characters',
      },
      show_password: false,
      message: "",
    };
  },
  methods: {

    logIn() {
      AuthorizationService.logIn(this.user)
        .then((response) => {
          let token = response.data.data.id;
          sessionStorage.setItem("auth_token", token);
          DataService.setToken(token);
          this.$router.push({name: "home"})
        })
        .catch((e) => {
          this.message = e.response.data.errors.find(x => x.detail !== "").detail;
        })
    },
  },
  mounted() {
    this.message = "";
  },
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
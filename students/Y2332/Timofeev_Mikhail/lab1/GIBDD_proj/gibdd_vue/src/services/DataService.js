import http from "../http-common";

class DataService {
  modelsName = "";
  auth_token = null;

  setModelsName(modelsName) {
    this.modelsName = modelsName
  }

  setToken(token) {
    this.auth_token = {
      headers: {
        Authorization: "Token " + token,
      }
    };
  }

  getAll() {
    return http.get(`/${this.modelsName}`, this.auth_token);
  }

  get(id) {
    return http.get(`/${this.modelsName}/${id}`, this.auth_token);
  }

  create(data) {
    return http.post(`/${this.modelsName}/`, data, this.auth_token);
  }

  update(id, data) {
    return http.put(`/${this.modelsName}/${id}/`, data, this.auth_token);
  }

  delete(id) {
    return http.delete(`/${this.modelsName}/${id}/`, this.auth_token);
  }

  find(search) {
    return http.get(`/${this.modelsName}?search=${search}`, this.auth_token);
  }
}

export default new DataService();
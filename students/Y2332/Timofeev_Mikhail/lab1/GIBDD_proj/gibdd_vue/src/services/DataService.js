import http from "../http-common";

class DataService {
  modelsName = "";

  setModelsName(modelsName) {
    this.modelsName = modelsName
  }

  getAll() {
    return http.get(`/${this.modelsName}`);
  }

  get(id) {
    return http.get(`/${this.modelsName}/${id}`);
  }

  create(data) {
    return http.post(`/${this.modelsName}/`, data);
  }

  update(id, data) {
    return http.put(`/${this.modelsName}/${id}/`, data);
  }

  delete(id) {
    return http.delete(`/${this.modelsName}/${id}/`);
  }

  find(search) {
    return http.get(`/${this.modelsName}?search=${search}`);
  }
}

export default new DataService();
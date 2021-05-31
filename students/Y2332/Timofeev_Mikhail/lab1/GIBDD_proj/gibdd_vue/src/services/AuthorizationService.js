import http from "../http-common";

class AuthorizationService {
    signUp(data) {
        return http.post("/auth/users/", data);
    }

    logIn(data) {
        return http.post("/auth/token/login/", data);
    }

    logOut() {
        return http.post("/auth/token/logout/", null, this.getToken());
    }

    getToken() {
        return {
            headers: {
                Authorization: "Token " + sessionStorage.getItem("auth_token"),
            }
        };
    }
}

export default new AuthorizationService();
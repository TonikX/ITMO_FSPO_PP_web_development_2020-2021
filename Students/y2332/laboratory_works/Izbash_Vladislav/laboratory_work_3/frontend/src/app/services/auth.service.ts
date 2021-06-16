import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { UserModel } from "../models/user.model";
import { Observable } from "rxjs";
import { map } from "rxjs/operators";

@Injectable({
    providedIn: 'root',
})
export class AuthService {
    private _httpHeaders = new HttpHeaders();

    constructor(private http: HttpClient) {
        let auth_token = localStorage.getItem("auth_token");
        if (auth_token) {
            this._httpHeaders = new HttpHeaders({
                    Authorization: `Token ${auth_token}`,
            });
        }
    }

    login(username: string, password: string): Observable<void> {
        return this.http.post("/api/token/login", {username, password})
            .pipe(map((result: any) => {
                localStorage.setItem("auth_token", result.auth_token);
                this._httpHeaders = new HttpHeaders({
                    Authorization: `Token ${result.auth_token}`,
                });
            }));
    }

    logout() {
        localStorage.removeItem("auth_token");
        this._httpHeaders = new HttpHeaders();
    }

    getCurrentUser(): Observable<UserModel> {
        return this.http.get<UserModel>("/api/users/me", {headers: this.httpHeaders});
    }

    get httpHeaders(): HttpHeaders {
        return this._httpHeaders;
    }
}

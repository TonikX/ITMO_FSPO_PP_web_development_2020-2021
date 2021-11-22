import { Inject, Injectable } from "@angular/core";
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { ModelInterface } from "../models/model.interface";
import { Observable } from "rxjs";
import { PageModel } from "../models/page.model";
import { AuthService } from "./auth.service";

@Injectable()
export class CrudService<M extends ModelInterface> {
    private url!: string;
    private readonly httpHeaders = new HttpHeaders();

    constructor(private http: HttpClient, private auth: AuthService) {}

    setEndpoint(endpoint: string) {
        this.url = `/api/${endpoint}/`;
    }

    list(
        offset: number,
        limit: number,
        ordering: string[] = [],
        search: string = "",
    ): Observable<PageModel<M>> {
        let params = new HttpParams()
            .set("offset", offset)
            .set("limit", limit)
            .set("ordering", ordering.join())
            .set("search", search);

        return this.http.get<PageModel<M>>(
            this.url,
            {params: params, headers: this.auth.httpHeaders},
        );
    }

    get(id: number): Observable<M> {
        return this.http.get<M>(this.url + id, {headers: this.auth.httpHeaders});
    }

    create(data: M): Observable<M> {
        return this.http.post<M>(this.url, data, {headers: this.auth.httpHeaders});
    }

    update(data: M): Observable<void> {
        return this.http.put<void>(this.url + data.id + "/", data, {headers: this.auth.httpHeaders});
    }

    delete(id: number): Observable<void> {
        return this.http.delete<void>(this.url + id, {headers: this.auth.httpHeaders});
    }
}
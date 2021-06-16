import { CollectionViewer, DataSource } from "@angular/cdk/collections";
import { ModelInterface } from "../models/model.interface";
import { BehaviorSubject, Observable, of } from "rxjs";
import { CrudService } from "./crud.service";
import { catchError, finalize } from "rxjs/operators";
import { PageModel } from "../models/page.model";

export class CrudDataSource<M extends ModelInterface> implements DataSource<M> {
    private entitySubject = new BehaviorSubject<M[]>([]);
    private loadingSubject = new BehaviorSubject<boolean>(false);

    total = 0;
    loading = this.loadingSubject.asObservable();

    constructor(private crud: CrudService<M>) {}

    connect(collectionViewer: CollectionViewer): Observable<M[]> {
        return this.entitySubject.asObservable();
    }

    disconnect(collectionViewer: CollectionViewer): void {
        this.entitySubject.complete();
        this.loadingSubject.complete();
    }

    load(offset: number, limit: number, ordering: string[] = [], search: string = "") {
        this.loadingSubject.next(true);

        this.crud.list(offset, limit, ordering, search).pipe(
            catchError(() => of([])),
            finalize(() => this.loadingSubject.next(false)),
        ).subscribe(res => {
            let page = <PageModel<M>> res;
            this.total = page.count;
            this.entitySubject.next(page.results);
        });
    }
}
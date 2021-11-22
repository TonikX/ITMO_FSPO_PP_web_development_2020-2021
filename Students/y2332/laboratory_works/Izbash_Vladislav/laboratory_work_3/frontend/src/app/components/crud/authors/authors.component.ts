import { AfterViewInit, Component, Inject, OnInit, TemplateRef, ViewChild } from "@angular/core";
import { CrudDataSource } from "../../../services/crud.datasource";
import { CrudService } from "../../../services/crud.service";
import { AuthorModel } from "../../../models/author.model";
import { MatSort } from "@angular/material/sort";
import { MatPaginator } from "@angular/material/paginator";
import { merge } from "rxjs";
import { tap } from "rxjs/operators";
import { MatDialog } from "@angular/material/dialog";
import { AuthorDialog } from "./author.dialog";
import { DeleteDialog } from "../delete.dialog";

@Component({
    selector: 'app-authors',
    templateUrl: 'authors.component.html',
})
export class AuthorsComponent implements OnInit, AfterViewInit {
    dataSource!: CrudDataSource<AuthorModel>;
    displayedColumns = ["id", "name", "actions"];

    @ViewChild(MatSort)
    sort!: MatSort;
    @ViewChild(MatPaginator)
    paginator!: MatPaginator;

    search = "";

    constructor(
        @Inject("AuthorService") private authors: CrudService<AuthorModel>,
        private dialog: MatDialog,
    ) {
        this.authors.setEndpoint("authors");
    }

    ngOnInit() {
        this.dataSource = new CrudDataSource<AuthorModel>(this.authors);
        this.dataSource.load(0, 5);
    }

    ngAfterViewInit() {
        this.sort.sortChange.subscribe(() => this.paginator.pageIndex = 0);

        merge(this.sort.sortChange, this.paginator.page)
            .pipe(tap(() => this.fetch()))
            .subscribe();
    }

    addRow() {
        this.dialog.open(AuthorDialog).afterClosed().subscribe(data => {
            if (data) {
                this.authors.create(data).subscribe();
                this.fetch();
            }
        });
    }

    updateRow(row: AuthorModel) {
        this.dialog.open(AuthorDialog, { data: row }).afterClosed().subscribe(data => {
            if (data) {
                this.authors.update(data).subscribe();
                this.fetch();
            }
        })
    }

    updateSearch(event: Event) {
        this.search = (event.target as HTMLInputElement).value;
        this.fetch();
    }

    deleteRow(row: AuthorModel) {
        this.dialog.open(DeleteDialog).afterClosed().subscribe(res => {
            if (res == "delete") {
                this.authors.delete(row.id).subscribe(_ => this.fetch());
            }
        });
    }

    private fetch() {
        let ordering: string[] = [];
        if (this.sort.direction == "asc") {
            ordering = [this.sort.active];
        } else if (this.sort.direction == "desc") {
            ordering = ["-" + this.sort.active];
        }

        this.dataSource.load(
            this.paginator.pageIndex * this.paginator.pageSize,
            this.paginator.pageSize,
            ordering,
            this.search,
        )
    }
}
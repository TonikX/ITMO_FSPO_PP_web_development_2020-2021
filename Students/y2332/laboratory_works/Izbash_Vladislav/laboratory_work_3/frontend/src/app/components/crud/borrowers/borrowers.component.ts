import { AfterViewInit, Component, Inject, OnInit, TemplateRef, ViewChild } from "@angular/core";
import { CrudDataSource } from "../../../services/crud.datasource";
import { CrudService } from "../../../services/crud.service";
import { AuthorModel } from "../../../models/author.model";
import { MatSort } from "@angular/material/sort";
import { MatPaginator } from "@angular/material/paginator";
import { merge } from "rxjs";
import { tap } from "rxjs/operators";
import { MatDialog } from "@angular/material/dialog";
import { DeleteDialog } from "../delete.dialog";
import { BookModel } from "../../../models/book.model";
import { BorrowerModel } from "../../../models/borrower.model";
import { BorrowerDialog } from "./borrower.dialog";

@Component({
    selector: 'app-books',
    templateUrl: 'borrowers.component.html',
})
export class BorrowersComponent implements OnInit, AfterViewInit {
    dataSource!: CrudDataSource<BorrowerModel>;
    displayedColumns = ["id", "firstname", "lastname", "patronymic", "birthdate", "address", "telnumber", "card_num", "actions"];

    @ViewChild(MatSort)
    sort!: MatSort;
    @ViewChild(MatPaginator)
    paginator!: MatPaginator;

    search = "";

    constructor(
        @Inject("BookService") private borrowers: CrudService<BorrowerModel>,
        private dialog: MatDialog,
    ) {
        this.borrowers.setEndpoint("borrowers");
    }

    ngOnInit() {
        this.dataSource = new CrudDataSource<BorrowerModel>(this.borrowers);
        this.dataSource.load(0, 5);
    }

    ngAfterViewInit() {
        this.sort.sortChange.subscribe(() => this.paginator.pageIndex = 0);

        merge(this.sort.sortChange, this.paginator.page)
            .pipe(tap(() => this.fetch()))
            .subscribe();
    }

    addRow() {
        this.dialog.open(BorrowerDialog).afterClosed().subscribe(data => {
            if (data) {
                this.borrowers.create(data).subscribe();
                this.fetch();
            }
        });
    }

    updateRow(row: BookModel) {
        this.dialog.open(BorrowerDialog, { data: row }).afterClosed().subscribe(data => {
            if (data) {
                this.borrowers.update(data).subscribe();
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
                this.borrowers.delete(row.id).subscribe(_ => this.fetch());
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
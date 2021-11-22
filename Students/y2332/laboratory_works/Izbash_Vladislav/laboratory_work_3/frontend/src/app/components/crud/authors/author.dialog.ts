import { Component, Inject } from "@angular/core";
import { MAT_DIALOG_DATA, MatDialogRef } from "@angular/material/dialog";
import { AuthorModel } from "../../../models/author.model";
import { FormControl, FormGroup } from "@angular/forms";
import { CrudService } from "../../../services/crud.service";

@Component({
    selector: 'app-author-form',
    templateUrl: 'author.dialog.html',
})
export class AuthorDialog {
    form: FormGroup;

    constructor(
        public dialog: MatDialogRef<AuthorDialog>,
        @Inject(MAT_DIALOG_DATA) public data?: AuthorModel,
    ) {
        if (this.data) {
            this.form = new FormGroup({
                name: new FormControl(this.data.name),
            });
        } else {
            this.form = new FormGroup({
                name: new FormControl(''),
            });
        }
    }

    apply() {
        if (this.data) {
            this.data.name = this.form.value.name;
        } else {
            this.data = new AuthorModel(this.form.value.name);
        }

        this.dialog.close(this.data);
    }
}
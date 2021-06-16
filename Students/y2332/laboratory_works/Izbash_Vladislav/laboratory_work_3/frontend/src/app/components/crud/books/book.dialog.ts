import { Component, Inject } from "@angular/core";
import { MAT_DIALOG_DATA, MatDialogRef } from "@angular/material/dialog";
import { FormControl, FormGroup } from "@angular/forms";
import { BookModel } from "../../../models/book.model";

@Component({
    selector: 'app-author-form',
    templateUrl: 'book.dialog.html',
})
export class BookDialog {
    form: FormGroup;

    constructor(
        public dialog: MatDialogRef<BookDialog>,
        @Inject(MAT_DIALOG_DATA) public data?: BookModel,
    ) {
        if (this.data) {
            this.form = new FormGroup({
                name: new FormControl(this.data.name),
                volume: new FormControl(this.data.volume),
                orig_lang: new FormControl(this.data.orig_lang),
                kind: new FormControl(this.data.kind),
                discipline: new FormControl(this.data.discipline),
                author: new FormControl(this.data.author),
                translator: new FormControl(this.data.translator),
            });
        } else {
            this.form = new FormGroup({
                name: new FormControl(''),
                volume: new FormControl(''),
                orig_lang: new FormControl(''),
                kind: new FormControl(''),
                discipline: new FormControl(''),
                author: new FormControl(''),
                translator: new FormControl(''),
            });
        }
    }

    apply() {
        if (this.data) {
            this.data.name = this.form.value.name;
            this.data.volume = this.form.value.volume;
            this.data.orig_lang = this.form.value.orig_lang;
            this.data.kind = this.form.value.kind;
            this.data.discipline = this.form.value.discipline;
            this.data.author = this.form.value.author;
            this.data.translator = this.form.value.translator;
        } else {
            this.data = new BookModel(
                this.form.value.name,
                this.form.value.volume,
                this.form.value.orig_lang,
                this.form.value.kind,
                this.form.value.discipline,
                this.form.value.author,
                this.form.value.translator,
            );
        }

        this.dialog.close(this.data);
    }
}
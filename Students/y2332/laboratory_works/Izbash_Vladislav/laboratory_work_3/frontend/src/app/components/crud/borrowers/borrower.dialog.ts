import { Component, Inject } from "@angular/core";
import { MAT_DIALOG_DATA, MatDialogRef } from "@angular/material/dialog";
import { FormControl, FormGroup } from "@angular/forms";
import { BorrowerModel } from "../../../models/borrower.model";

@Component({
    selector: 'app-author-form',
    templateUrl: 'borrower.dialog.html',
})
export class BorrowerDialog {
    form: FormGroup;

    constructor(
        public dialog: MatDialogRef<BorrowerDialog>,
        @Inject(MAT_DIALOG_DATA) public data?: BorrowerModel,
    ) {
        if (this.data) {
            this.form = new FormGroup({
                firstname: new FormControl(this.data.firstname),
                lastname: new FormControl(this.data.lastname),
                patronymic: new FormControl(this.data.patronymic),
                birthdate: new FormControl(this.data.birthdate),
                address: new FormControl(this.data.address),
                telnumber: new FormControl(this.data.telnumber),
                card_num: new FormControl(this.data.card_num),
            });
        } else {
            this.form = new FormGroup({
                firstname: new FormControl(''),
                lastname: new FormControl(''),
                patronymic: new FormControl(''),
                birthdate: new FormControl(''),
                address: new FormControl(''),
                telnumber: new FormControl(''),
                card_num: new FormControl(''),
            });
        }
    }

    apply() {
        if (this.data) {
            this.data.firstname = this.form.value.firstname;
            this.data.lastname = this.form.value.lastname;
            this.data.patronymic = this.form.value.patronymic;
            this.data.birthdate = this.form.value.birthdate;
            this.data.address = this.form.value.address;
            this.data.telnumber = this.form.value.telnumber;
            this.data.card_num = this.form.value.card_num;
        } else {
            this.data = new BorrowerModel(
                this.form.value.firstname,
                this.form.value.lastname,
                this.form.value.patronymic,
                this.form.value.birthdate,
                this.form.value.address,
                this.form.value.telnumber,
                this.form.value.card_num,
            );
        }

        this.dialog.close(this.data);
    }
}
import { ModelInterface } from "./model.interface";

export class BorrowerModel implements ModelInterface {
    public id: number;

    constructor(
        public firstname: string,
        public lastname: string,
        public patronymic: string,
        public birthdate: string,
        public address: string,
        public telnumber: string,
        public card_num: string,
    ) {
        this.id = -1;
    }
}
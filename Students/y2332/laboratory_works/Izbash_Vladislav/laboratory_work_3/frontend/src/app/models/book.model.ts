import { ModelInterface } from "./model.interface";

export class BookModel implements ModelInterface {
    public id: number;

    constructor(
        public name: string,
        public volume: number,
        public orig_lang: string,
        public kind: string,
        public discipline: string,
        public author: number,
        public translator: number,
    ) {
        this.id = -1;
    }
}
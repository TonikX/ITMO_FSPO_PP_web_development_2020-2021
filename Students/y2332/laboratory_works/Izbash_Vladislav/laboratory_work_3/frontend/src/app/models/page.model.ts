import { ModelInterface } from "./model.interface";

export class PageModel<M extends ModelInterface> {
    constructor(
        public count: number,
        public next: string,
        public previous: string,
        public results: M[],
    ) {}
}
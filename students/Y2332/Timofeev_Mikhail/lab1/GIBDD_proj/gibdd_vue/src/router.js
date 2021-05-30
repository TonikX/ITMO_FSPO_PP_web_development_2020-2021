import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/bodies",
      name: "bodies",
      component: () => import("./components/Body/BodiesList")
    },
    {
      path: "/bodies/:id",
      name: "body",
      component: () => import("./components/Body/Body")
    },
    {
      path: "bodies/add",
      name: "add-body",
      component: () => import("./components/Body/AddBody")
    },
    {
      path: "/engines",
      name: "engines",
      component: () => import("./components/Engine/EnginesList")
    },
    {
      path: "/engines/:id",
      name: "engine",
      component: () => import("./components/Engine/Engine")
    },
    {
      path: "engines/add",
      name: "add-engine",
      component: () => import("./components/Engine/AddEngine")
    },
    {
      path: "/models",
      name: "models",
      component: () => import("./components/Model/ModelsList")
    },
    {
      path: "/models/:id",
      name: "model",
      component: () => import("./components/Model/Model")
    },
    {
      path: "models/add",
      name: "add-model",
      component: () => import("./components/Model/AddModel")
    },
    {
      path: "/lOwners",
      name: "lOwners",
      component: () => import("./components/LegalOwner/LOwnersList")
    },
    {
      path: "/lOwners/:id",
      name: "lOwner",
      component: () => import("./components/LegalOwner/LOwner")
    },
    {
      path: "lOwners/add",
      name: "add-lOwner",
      component: () => import("./components/LegalOwner/AddLOwner")
    },
    {
      path: "/pOwners",
      name: "pOwners",
      component: () => import("./components/PhysicalOwner/POwnersList")
    },
    {
      path: "/pOwners/:id",
      name: "pOwner",
      component: () => import("./components/PhysicalOwner/POwner")
    },
    {
      path: "pOwners/add",
      name: "add-pOwner",
      component: () => import("./components/PhysicalOwner/AddPOwner")
    },
    {
      path: "/inspectors",
      name: "inspectors",
      component: () => import("./components/Inspector/InspectorsList")
    },
    {
      path: "/inspectors/:id",
      name: "inspector",
      component: () => import("./components/Inspector/Inspector")
    },
    {
      path: "inspectors/add",
      name: "add-inspector",
      component: () => import("./components/Inspector/AddInspector")
    },
    {
      path: "/cars",
      name: "cars",
      component: () => import("./components/Car/CarsList")
    },
    {
      path: "/cars/:id",
      name: "car",
      component: () => import("./components/Car/Car")
    },
    {
      path: "cars/add",
      name: "add-car",
      component: () => import("./components/Car/AddCar")
    },
    {
      path: "/away-list",
      name: "away-list",
      component: () => import("./components/DriveAway/AwayList")
    },
    {
      path: "/away-list/:id",
      name: "away",
      component: () => import("./components/DriveAway/Away")
    },
    {
      path: "away-list/add",
      name: "add-away",
      component: () => import("./components/DriveAway/AddAway")
    },
    {
      path: "/watch-list",
      name: "watch-list",
      component: () => import("./components/Watch/WatchesList")
    },
    {
      path: "/watch-list/:id",
      name: "watch",
      component: () => import("./components/Watch/Watch")
    },
    {
      path: "watch-list/add",
      name: "add-watch",
      component: () => import("./components/Watch/AddWatch")
    }
  ]
});
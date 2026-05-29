import express from "express";
const routerAdmin = express.Router(); // router methodini chaqirb olamz
import restaurantController from "./controllers/restaurant.controller";

// router instance dan foydalanib get post methodini amalga oshramz
routerAdmin.get("/", restaurantController.goHome);

routerAdmin.get("/login", restaurantController.getLogin);

routerAdmin.get("/signup", restaurantController.getSignup);

export default routerAdmin;

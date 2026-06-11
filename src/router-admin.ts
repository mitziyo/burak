import express from "express";
const routerAdmin = express.Router(); // router methodini chaqirb olamz
import restaurantController from "./controllers/restaurant.controller";
import productController from "./controllers/product.controller";

// router instance dan foydalanib get post methodini amalga oshramz
/** Restaurant*/
routerAdmin.get("/", restaurantController.goHome);
routerAdmin
  .get("/login", restaurantController.getLogin)
  .post("/login", restaurantController.processLogin);

routerAdmin
  .get("/signup", restaurantController.getSignup)
  .post("/signup", restaurantController.processSignup);
routerAdmin.get("/logout", restaurantController.logout);
routerAdmin.get("/check-me", restaurantController.checkAuthSession);

/** Product */
routerAdmin.get(
  "/product/all",
  restaurantController.verifyRestaurant,
  productController.getAllProducts,
);
routerAdmin.get(
  "/product/create",
  restaurantController.verifyRestaurant,
  productController.createNewProduct,
);
routerAdmin.get(
  "/product/:id",
  restaurantController.verifyRestaurant,
  productController.updatedChosenProduct,
);

/** User */

export default routerAdmin;

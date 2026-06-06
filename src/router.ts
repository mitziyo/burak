import express from "express";
const router = express.Router(); // router methodini chaqirb olamz
import memberController from "./controllers/member.controller";

// router instance dan foydalanib get post methodini amalga oshramz
// router.get("/", memberController.goHome);

// router.get("/login", memberController.getLogin);

// router.get("/signup", memberController.getSignup);

router.post("/login", memberController.login);

router.post("/signup", memberController.signup);

export default router;

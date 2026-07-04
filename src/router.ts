import express from "express";
const router = express.Router(); // router methodini chaqirb olamz
import memberController from "./controllers/member.controller";

// router instance dan foydalanib get post methodini amalga oshramz
// router.get("/", memberController.goHome);

// router.get("/login", memberController.getLogin);

// router.get("/signup", memberController.getSignup);

/***** Member *****/

router.post("/member/login", memberController.login);
router.post("/member/signup", memberController.signup);
router.post(
  "/member/logout",
  memberController.verifyAuth,
  memberController.logout,
);
router.get(
  "/member/detail",
  memberController.verifyAuth,
  memberController.getMemberDetail,
);

/***** Product *****/

/***** Order *****/
export default router;

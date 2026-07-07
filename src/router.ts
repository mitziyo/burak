import express from "express";
const router = express.Router(); // router methodini chaqirb olamz
import memberController from "./controllers/member.controller";
import uploader from "./libs/utils/uploader";

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

router.post(
  "/member/update",
  memberController.verifyAuth,
  uploader("members").single("memberImage"),
  memberController.updateMember,
);

router.get("/member/top-users", memberController.getTopUsers);

/***** Product *****/

/***** Order *****/
export default router;

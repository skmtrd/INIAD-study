let BASE_URL = "https://edu-iot.iniad.org/api/v1";

function displayLockerPosition(result) {
  let lockerResult = document.getElementById("locker-result");
  let lockerAddress = document.getElementById("locker-address");
  let lockerFloor = document.getElementById("locker-floor");

  if (result.status === "success") {
    lockerResult.innerHTML = result.status;
    lockerAddress.innerHTML = result.lockerAddress;
    lockerFloor.innerHTML = result.lockerFloor;
  } else {
    lockerResult.innerHTML = result.status;
    lockerAddress.innerHTML = "none";
    lockerFloor.innerHTML = "none";
  }
}

function displayIccardInformation(result) {
  let iccardResult = document.getElementById("iccard-result");
  let iccardList = document.getElementById("iccard-id");
  let iccardComment = document.getElementById("iccard-comment");

  if (result.status === "success") {
    iccardResult.innerHTML = result.status;
    iccardComment.innerHTML = result.iccardComment;
    iccardList.innerHTML = result.iccardId;
  } else {
    iccardResult.innerHTML = `${result.status}`;
    iccardComment.innerHTML = "none";
    iccardList.innerHTML = "none";
  }
}

function getLockerPosition() {
  let userid = document.getElementById("iniad-id").value;
  let userpw = document.getElementById("iniad-pw").value;
  let url = BASE_URL + "/locker";
  callLockerPositionAPI(url, "GET", userid, userpw, displayLockerPosition);
}

function getRegisteredIccard() {
  let userid = document.getElementById("iniad-id").value;
  let userpw = document.getElementById("iniad-pw").value;
  let url = BASE_URL + "/iccards";
  callRegisteredIccardAPI(url, "GET", userid, userpw, displayIccardInformation);
}

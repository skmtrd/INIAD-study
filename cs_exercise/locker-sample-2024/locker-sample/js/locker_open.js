function displayIccardRegisterResult(result) {
  console.log(result);
  let resultElement = document.getElementById("register-result");
  if (result.status === "success") {
    resultElement.innerHTML = result.description;
  } else {
    resultElement.innerHTML = "Failed: " + result.description;
  }
}

function displayIccardDeleteResult(result) {
  let resultElement = document.getElementById("delete-result");
  if (result.status === "success") {
    resultElement.innerHTML = result.description;
  } else {
    resultElement.innerHTML = "Failed: " + result.description;
  }
}

function registerIccard() {
  let userid = document.getElementById("iniad-id").value;
  let userpw = document.getElementById("iniad-pw").value;
  let iccardId = document.getElementById("register-iccard-num").value;
  let iccardComment = document.getElementById("register-iccard-comment").value;
  let iccardData = {
    uid: iccardId,
    comment: iccardComment,
  };
  let url = BASE_URL + "/iccards";
  callIccardAPI(
    url,
    "POST",
    iccardData,
    userid,
    userpw,
    displayIccardRegisterResult
  );
}

function deleteIccard() {
  let userid = document.getElementById("iniad-id").value;
  let userpw = document.getElementById("iniad-pw").value;
  let url = BASE_URL + "/iccards";
  callIccardAPI(url, "DELETE", null, userid, userpw, displayIccardDeleteResult);
}

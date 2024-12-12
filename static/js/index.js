document.getElementById("reviewForm").onsubmit = async function (event) {
  event.preventDefault();
  const formData = new FormData(this);
  const response = await fetch("/analyze", {
    method: "POST",
    body: formData,
  });
  const result = await response.json();

  // Show both containers
  document.getElementById("summary-container").style.display = "block";
  document.getElementById("sentiment-container").style.display = "block";

  // Update content
  document.getElementById("summarize").innerHTML = `${result.summarize}`;
  document.getElementById("result").innerText = `${result.sentiment} (${result.score.toFixed(2)})`;
  document.getElementById("starRating").innerHTML = getStarRating(result.score);

  // Handle positive points
  const positiveContainer = document.getElementById("positive-container");
  const positiveList = document.getElementById("positive-points");
  positiveList.innerHTML = "";

  if (result.key.positive && result.key.positive.length > 0) {
    result.key.positive.forEach((point) => {
      const li = document.createElement("li");
      li.className = "list-group-item";
      li.innerHTML = `<i class="fas fa-check-circle text-success mr-2"></i>${point}`;
      positiveList.appendChild(li);
    });
    positiveContainer.style.display = "block";
  } else {
    positiveContainer.style.display = "none";
  }

  // Handle negative points
  const negativeContainer = document.getElementById("negative-container");
  const negativeList = document.getElementById("negative-points");
  negativeList.innerHTML = "";

  if (result.key.negative && result.key.negative.length > 0) {
    result.key.negative.forEach((point) => {
      const li = document.createElement("li");
      li.className = "list-group-item";
      li.innerHTML = `<i class="fas fa-times-circle text-danger mr-2"></i>${point}`;
      negativeList.appendChild(li);
    });
    negativeContainer.style.display = "block";
  } else {
    negativeContainer.style.display = "none";
  }
};

function getStarRating(score) {
  let stars = "";
  for (let i = 0; i < 5; i++) {
    if (score >= (i + 1) * 1) {
      stars += '<i class="fas fa-star"></i>'; // Full star
    } else if (score >= i + 0.5) {
      stars += '<i class="fas fa-star-half-alt"></i>'; // Half star
    } else {
      stars += '<i class="far fa-star"></i>'; // Empty star
    }
  }
  return stars;
}
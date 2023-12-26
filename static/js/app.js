
        // Функция для фильтрации карточек по дате
        function filterByDate(startDate, endDate, cardDate) {
            if (!startDate || !endDate) {
                return true; // Если даты не заданы, не фильтруем по дате
            }

            var cardDateTime = new Date(cardDate).getTime();
            var startDateTime = new Date(startDate).getTime();
            var endDateTime = new Date(endDate).getTime();

            return (cardDateTime >= startDateTime && cardDateTime <= endDateTime);
        }

        // Функция для фильтрации карточек по выбранному значению в <select> и дате
        function filterResults() {
            var selectedDirection = document.getElementById("directionSelect").value;
            var startDate = document.getElementById("startDate").value;
            var endDate = document.getElementById("endDate").value;
            var cards = document.querySelectorAll(".card");

            cards.forEach(function(card) {
                var cardDirection = card.querySelector(".card__direction").innerText.trim();
                var cardDate = card.querySelector(".card__date").innerText.trim();

                // Проверяем условия для фильтрации по направлению
                var directionCondition = (selectedDirection === "all" || selectedDirection === cardDirection);

                // Проверяем условия для фильтрации по дате с использованием отдельной функции
                var dateCondition = filterByDate(startDate, endDate, cardDate);

                // Показываем или скрываем карточку в зависимости от выбранных условий
                if (directionCondition && dateCondition) {
                    card.style.display = "flex";
                } else {
                    card.style.display = "none";
                }
            });
        }
        function filterParts() {
            var selectedOption = document.getElementById("data__select").value;
            var cards = document.querySelectorAll(".card");
        
            cards.forEach(function(card) {
                var cardDate = card.querySelector(".card__date").textContent;
        
                if (selectedOption === "all" || selectedOption === cardDate) {
                    card.style.display = "flex";
                } else {
                    card.style.display = "none";
                }
            });
        }
        function filterJury() {
            var selectedOption = document.getElementById("data__select").value;
            var cards = document.querySelectorAll(".card");
        
            cards.forEach(function(card) {
                var cardDate = card.querySelector(".card__creator").textContent;
                console.log(cardDate)
        
                if (selectedOption === "all" || selectedOption === cardDate) {
                    card.style.display = "flex";
                } else {
                    card.style.display = "none";
                }
            });
        }
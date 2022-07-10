

(def seconds-in-one-year (* 365 24 60 60))

(println (* 1 seconds-in-one-year))
(println (* 2 seconds-in-one-year))
(println (* 5 seconds-in-one-year))
(println (* 10 seconds-in-one-year))


(+ 1 1)

(reduce #'+ '(1 1))


(defn create-input
  [arg]
  (->> (.split arg " ")
       (map #(Integer/parseInt %))))


(create-input "1 1")

(map #'Long/parseLong (.split "1 1" " "))

(reduce #'+ (create-input "1 1 1"))


(.split "1 + 2" "")
(map #(Integer/parseInt %) (clojure.string/split "1 2" #" "))

(let [[a op b] (clojure.string/split "1 + 1" #" ")])


(eval (list (read-string "+") 1 1))


;; clojureでcase文をつくる
(def sum '+)
(def dif '-)
(def mul '*)


(defn div
  [a b]
  (if (= b 0)
    "error"
    (quot a b)))


(defn c
  [n a b]
  (cond
    (= "+" n) (sum a b)
    (= "-" n) (dif a b)
    (= "*" n) (mul a b)
    (= "/" n) (div a b)
    :else "error"))



(def sum #'+)
(def dif #'-)
(def mul #'*)


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


(let [[a op b] (clojure.string/split (read-line) #" ")]
  (println (c op (Long/parseLong a) (Long/parseLong b))))

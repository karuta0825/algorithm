(use '[clojure.string :refer [split join]])
(require '[clojure.set :as set])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


;; 同じ要素を含んでいるのであればこのやり方はまずいですね
(defn intersection
  [a b]
  (set/intersection (set a) (set b)))


(defn union_set
  [a b]
  (sort < (set/union (set a) (set b))))


(defn substract
  [a b]
  (sort < (set/difference (set a) (set b))))


(defn symmetric_diff
  [a b]
  (let [interset (intersection a b)]
    (set/union (set/difference (set a) interset)
               (set/difference (set b) interset))))


(defn increment
  [a]
  (set (map #(mod (inc %1) 50) a)))


(defn decrement
  [a]
  (set (map #(mod (dec %1) 50) a)))


(def command
  {"intersection" intersection
   "union_set" union_set
   "symmetric_diff" symmetric_diff})


(set (list 1))


(let [_ (Integer/parseInt (read-line))
      a (create-input (read-line))
      _ (Integer/parseInt (read-line))
      b (create-input (read-line))
      [operation arg] (split (read-line) #" ")]

  (println (join " " (cond
                       (= operation "subtract") (substract a (list (Integer/parseInt arg)))
                       (= operation "increment") (increment a)
                       (= operation "decrement") (decrement a)
                       :else (apply (get command operation) (list a b))))))



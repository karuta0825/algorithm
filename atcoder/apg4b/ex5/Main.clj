;; (defn create-input
;;   [arg]
;;   (->> (.split arg " ")
;;        (map #(Integer/parseInt %))))

(defn create-input
  [arg]
  (->> (clojure.string/split arg #" ")
       (map #(Integer/parseInt %))))


(println (reduce #'+ (create-input (read-line))))


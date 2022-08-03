(use '[clojure.string :refer [split join]])


(defn ss
  [str result]
  (if (= (count str) 0)
    result
    (let [c (first str)
          num (count (take-while (fn [v] (= c v)) str))]
      (recur (join "" (drop num str)) (conj result [c num])))))


(let [one (read-line)
      two (read-line)
      so (ss one [])
      st (ss two [])]
  (when (= (map second so) (map second st))
    (println "No"))

  (println (if (some true? (map (fn [a b]
                                  (or (not (= (first a) (first b)))
                                      (and (= (second a) 1) (< (second a) (second b)))))
                                so st))
             "No"
             "Yes")))


;; このやり方でも駄目です
;; (defn s2
;;   [str]
;;   (reduce (fn [acc c]
;;             (let [[lc ln] (peek acc)]
;;               (if (= lc c)
;;                 (conj (vec (drop-last 1 acc)) [lc (inc ln)])
;;                 (conj acc [c 1])))) [] str))


;; (let [one (read-line)
;;       two (read-line)]
;;   (println (if (some true? (map (fn [a b]
;;                                   (or (not (= (first a) (first b)))
;;                                       (and (= (second a) 1) (< (second a) (second b)))))
;;                                 (s2 one) (s2 two)))
;;              "No"
;;              "Yes")))


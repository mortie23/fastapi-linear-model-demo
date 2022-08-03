library(plumber)

#* Return the estimated weight
#* @param height the height
#* @get /weight
function(height) {
  0.5772 * as.numeric(height) - 25.165
}

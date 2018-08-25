service APIsvc {
 string getTop()
 string getTopNoCache()
 string getGifs()
 string getGifsPaginated(1:i32 page)
}
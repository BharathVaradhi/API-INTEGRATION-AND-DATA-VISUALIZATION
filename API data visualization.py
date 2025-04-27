from imdb import IMDb            
import matplotlib.pyplot as plt   

movie_input = input("🎥 Enter movie names separated by commas (e.g. Inception, Tenet, Interstellar):\n")
movie_names = [movie.strip() for movie in movie_input.split(',')]  

imdb_client = IMDb()     
movie_titles = []          
movie_ratings = []

for name in movie_names:
    search_result = imdb_client.search_movie(name) 
    if search_result:
        movie_info = search_result[0]               
        movie_id = movie_info.movieID              
        movie_details = imdb_client.get_movie(movie_id) 
        rating = movie_details.get('rating')            
        title = movie_details.get('title')              
        if rating:
            movie_titles.append(title)
            movie_ratings.append(rating)
            print(f"✅ {title}: {rating}")
        else:
            print(f"⚠️ {name}: No rating available")
    else:
        print(f"❌ {name}: Not found")

if movie_titles:
    
    plt.figure(figsize=(10,5))

   
    plt.bar(movie_titles, movie_ratings, color='red', edgecolor='black', width=0.6)

    
    for index, value in enumerate(movie_ratings):
        plt.text(index, value + 0.2, str(value), ha='center', va='bottom',
                 fontdict={'size': 8, 'weight': 'bold'})


    title_font = {'family': 'serif', 'color': 'darkred', 'size': 16, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': 'darkblue', 'size': 13}

  
    plt.xlabel("Movie Titles", fontdict=label_font)
    plt.ylabel("IMDb Rating", fontdict=label_font)
    plt.title("IMDb Ratings of Your Favorite Movies", fontdict=title_font)
    plt.ylim(0,10)
   
    plt.tight_layout()

    
    plt.show()
else:
    print("❗ No valid movies to display.")

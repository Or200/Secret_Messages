def split_stories():
    with open("stories") as f:
        for i, line in enumerate(f.readlines()):
            if i % 2 == 0:
                with open("story_A.txt", "a") as f:
                    f.write(line)
            else:
                with open("story_B.txt", "a") as f:
                    f.write(line)


split_stories()
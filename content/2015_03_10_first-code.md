Title: First code sample
Date: 2015-03-10 17:46
Category: programming

I'm trying out the syntax highlighting extension to markdown available in
pelican. Here it goes

    :::cpp
    #include <vector>

    int main()
    {
        std::vector c = { 1, 2, 3 };
        for (auto&& e : c) {
            e -= 1;
        }
        return c[2];
    }

Now let's see how this looks.

#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

struct Photo
{
    int id = -1;
    int id2 = -1;
    bool vertical = false;
    set<int> tags;
    int unique_tags = 0;

    void merge(Photo &other)
    {
        auto i = tags.begin();
        // set()
        for (auto &&ot : other.tags)
            tags.insert(ot);
        vertical = false;
        id2 = other.id;

        unique_tags += other.unique_tags;
    }
};

ostream &operator<<(ostream &os, const Photo &p)
{
    os << "<Photo #" << p.id << ' ' << (p.vertical ? 'V' : 'H') << ", " << p.tags.size() << " tags:";
    for (auto &&tag : p.tags)
        os << ' ' << tag;
    if (p.unique_tags)
        os << ", " << p.unique_tags << " unique";
    os << '>';
    return os;
}

template <class T>
size_t common(T a, T b)
{
    size_t c = 0;
    auto x = a.begin();
    auto y = b.begin();
    while (x != a.end() && y != b.end())
    {
        if (*x < *y)
            ++x;
        else if (*x == *y)
        {
            ++c;
            ++x;
            ++y;
        }
        else
            ++y;
    }
    return c;
}

template <class T>
size_t score(T a, T b)
{
    // min(a, b, common), with a = size_a - common and b = size_b - common
    // == min(A - common, B - common, common)
    // == min(min(A, B) - common, common)
    size_t c = common(a, b);
    return min(min(a.size(), b.size()) - c, c);
}

void parse_input(vector<Photo> &photos)
{
    map<string, int> all_tags; // map tags to ints
    vector<int> tag_counter;   // count the occurence of each tag

    int current_id = -1;
    for (auto &&photo : photos)
    {
        photo.id = ++current_id;
        char orient;
        cin >> orient;
        photo.vertical = orient == 'V';
        int tag_count;
        cin >> tag_count;
        // photo.tags.resize(tag_count);
        // for (auto &&tag : photo.tags)
        for (size_t i = 0; i < tag_count; ++i)
        {
            int tag;
            string tag_str;
            cin >> tag_str;
            auto tag_id = all_tags.find(tag_str);
            if (tag_id == all_tags.end())
            {
                tag = all_tags.size();
                all_tags.emplace(tag_str, tag);
                tag_counter.push_back(1);
            }
            else
            {
                tag = tag_id->second;
                ++tag_counter[tag];
            }
            photo.tags.insert(tag);
        }
        // sort(photo.tags.begin(), photo.tags.end());

        // cout << photo << endl;
    }

    cout << "tag occurence";
    for (auto &&count : tag_counter)
        cout << ' ' << count;
    cout << endl;
}

void merge_verticals(vector<Photo> &photos)
{
    Photo *last = nullptr;
    // for (auto p : photos)
    for (auto p = photos.begin(); p != photos.end(); ++p)
    {
        if (!p->vertical)
            continue;
        if (last == nullptr)
            last = &(*p);
        else
        {
            last->merge(*p);
            photos.erase(p);
            last = nullptr;
        }
    }
}

int main()
{
    int photo_count;
    cin >> photo_count;

    vector<Photo> photos(photo_count);
    parse_input(photos);
    merge_verticals(photos);

    // cout << "merged" << endl;
    // for (auto &&p : photos)
    //     cout << p << endl;

    for (size_t _first = 0; _first < photos.size() - 1; ++_first)
    {
        auto first = photos[_first];
        cout << '#' << first.id;
        for (size_t _second = _first + 1; _second < photos.size(); ++_second)
        {
            auto second = photos[_second];
            // cout << "first " << _first << " second " << _second;
            int s = score(first.tags, second.tags);
            // cout << ' ' << s;
        }
        cout << '\n';
    }

    return 0;
}

'use client';

import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { getPosts, getTags } from '@/lib/api';
import { useLanguage } from '@/context/LanguageContext';
import Link from 'next/link';
import { Search, Tag as TagIcon } from 'lucide-react';

export default function BlogPage() {
  const { t, lang } = useLanguage();
  const [posts, setPosts] = useState([]);
  const [tags, setTags] = useState([]);
  const [search, setSearch] = useState('');
  const [selectedTag, setSelectedTag] = useState('');

  useEffect(() => {
    getTags().then(res => setTags(res.data.results));
  }, []);

  useEffect(() => {
    getPosts({ search, tags__slug: selectedTag }).then(res => setPosts(res.data.results));
  }, [search, selectedTag]);

  return (
    <div className="container-custom py-20">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-8 mb-12">
        <h1 className="text-4xl font-bold">{t.blog.title}</h1>
        
        <div className="flex flex-col sm:flex-row gap-4">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input 
              type="text" 
              placeholder={t.blog.search}
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="pl-10 pr-4 py-2 border rounded-full w-full sm:w-64 focus:ring-2 focus:ring-blue-600 outline-none transition-all dark:bg-gray-800"
            />
          </div>
          <div className="flex items-center gap-2 overflow-x-auto pb-2 sm:pb-0 scrollbar-hide">
            <button 
              onClick={() => setSelectedTag('')}
              className={`px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-colors ${!selectedTag ? 'bg-blue-600 text-white' : 'bg-gray-100 dark:bg-gray-800 hover:bg-gray-200'}`}
            >
              All
            </button>
            {tags.map(tag => (
              <button 
                key={tag.slug}
                onClick={() => setSelectedTag(tag.slug)}
                className={`px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-colors ${selectedTag === tag.slug ? 'bg-blue-600 text-white' : 'bg-gray-100 dark:bg-gray-800 hover:bg-gray-200'}`}
              >
                {tag.name}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {posts.map((post, index) => (
          <motion.article 
            key={post.slug}
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: index * 0.05 }}
            className="group block p-8 bg-white dark:bg-gray-800 border rounded-2xl hover:border-blue-600 transition-all hover:shadow-lg"
          >
            <div className="flex items-center gap-4 text-sm text-gray-500 mb-4 transition-colors">
              <span className="bg-gray-100 dark:bg-gray-700 px-3 py-1 rounded-full text-blue-600 font-bold">
                {new Date(post.published_at).toLocaleDateString()}
              </span>
              <div className="flex gap-2">
                {post.tags.map(tag => (
                  <span key={tag.slug} className="flex items-center gap-1"><TagIcon className="w-3 h-3" />{tag.name}</span>
                ))}
              </div>
            </div>
            <h2 className="text-2xl font-bold mb-3 group-hover:text-blue-600 transition-colors">
              {lang === 'en' ? post.title_en : post.title_uk}
            </h2>
            <p className="text-gray-600 dark:text-gray-400 mb-6 line-clamp-3">
              {lang === 'en' ? post.excerpt_en : post.excerpt_uk}
            </p>
            <Link href={`/blog/${post.slug}`} className="font-bold text-blue-600 flex items-center gap-2 group-hover:gap-3 transition-all">
              {t.blog.read_more} →
            </Link>
          </motion.article>
        ))}
      </div>
    </div>
  );
}

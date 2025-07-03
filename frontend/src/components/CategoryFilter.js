import React, { useEffect, useState } from 'react';
import api from '../services/api';

const CategoryFilter = ({ selectedCategory, onSelectCategory }) => {
  const [categories, setCategories] = useState([]);
  const [expandedCategory, setExpandedCategory] = useState(null);
  const [expandedSubCategory, setExpandedSubCategory] = useState(null);

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await api.get('/listings/categories');
      setCategories(response.data);
    } catch (error) {
      console.error('Erreur lors du chargement des catégories', error);
    }
  };

  const handleCategoryClick = (categoryName) => {
    if (expandedCategory === categoryName) {
      setExpandedCategory(null);
      setExpandedSubCategory(null);
    } else {
      setExpandedCategory(categoryName);
      setExpandedSubCategory(null);
    }
  };

  const handleSubCategoryClick = (subCategoryName) => {
    if (expandedSubCategory === subCategoryName) {
      setExpandedSubCategory(null);
    } else {
      setExpandedSubCategory(subCategoryName);
    }
  };

  const handleSelect = (category, subCategory) => {
    onSelectCategory(category, subCategory);
  };

  return (
    <div className="mb-4">
      <h2 className="font-semibold mb-2">Catégories</h2>
      <ul>
        {categories.map((cat) => (
          <li key={cat.name} className="mb-2">
            <button
              className="font-bold text-indigo-600 hover:underline"
              onClick={() => handleCategoryClick(cat.name)}
            >
              {cat.name}
            </button>
            {expandedCategory === cat.name && cat.subcategories && (
              <ul className="ml-4 mt-1">
                {cat.subcategories.map((sub) => (
                  <li key={sub.name} className="mb-1">
                    <button
                      className="text-indigo-500 hover:underline"
                      onClick={() => handleSelect(cat.name, sub.name)}
                    >
                      {sub.name}
                    </button>
                    {sub.subcategories && expandedSubCategory === sub.name && (
                      <ul className="ml-4 mt-1">
                        {sub.subcategories.map((subsub) => (
                          <li key={subsub.name} className="mb-1">
                            <button
                              className="text-indigo-400 hover:underline"
                              onClick={() => handleSelect(cat.name, subsub.name)}
                            >
                              {subsub.name}
                            </button>
                          </li>
                        ))}
                        <li>
                          <button
                            className="text-indigo-400 italic hover:underline"
                            onClick={() => handleSelect(cat.name, 'Voir tout')}
                          >
                            [Voir tout]
                          </button>
                        </li>
                        <li>
                          <button
                            className="text-indigo-400 italic hover:underline"
                            onClick={() => handleSelect(cat.name, 'Autre')}
                          >
                            [Autre]
                          </button>
                        </li>
                      </ul>
                    )}
                  </li>
                ))}
                <li>
                  <button
                    className="text-indigo-500 italic hover:underline"
                    onClick={() => handleSelect(cat.name, 'Voir tout')}
                  >
                    [Voir tout]
                  </button>
                </li>
                <li>
                  <button
                    className="text-indigo-500 italic hover:underline"
                    onClick={() => handleSelect(cat.name, 'Autre')}
                  >
                    [Autre]
                  </button>
                </li>
              </ul>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryFilter;
